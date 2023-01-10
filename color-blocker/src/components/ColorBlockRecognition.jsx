import React, { useEffect, useRef, useState } from "react";
import CapturedImage from "./CapturedImage";
import TagIdentifier from "./TagIdentifier";

/*Componente que renderiza um componente de vídeo e uma imagem em tela.
 O vídeo é obtido a partir da câmera do usuário e, a cada 100ms, uma imagem é capturada a partir dele e armazenada no estado "data".
 Também é possível selecionar uma cor através de um input do tipo "color", que é armazenada no estado "color".
 Quando "data" possui um valor, o componente "CapturedImage" é renderizado passando como propriedades a cor selecionada ("targetColor") e a imagem capturada ("image").

O gerenciamento de estado é feito através das funções de Hooks "useState" e "useRef".
O efeito do Hook "useEffect" é utilizado para iniciar a transmissão do vídeo da câmera e para capturar uma imagem a cada 100ms.
 */

function ColorBlockRecognition() {
  const [data, setData] = useState(null);
  const [color, setColor] = useState({
    r: 0,
    g: 0,
    b: 0,
  });

  const videoRef = useRef(null);

  async function handleRecogColor() {
    const canvas = document.createElement("canvas");
    canvas.width = videoRef.current.videoWidth;
    canvas.height = videoRef.current.videoHeight;
    canvas.getContext("2d").drawImage(videoRef.current, 0, 0);
    const image = canvas.toDataURL("image/jpeg");
    setData(image);
  }

  useEffect(() => {
    async function streamVideo() {
      const stream = await navigator.mediaDevices.getUserMedia({
        video: true,
      });
      videoRef.current.srcObject = stream;
    }

    streamVideo();
  }, []);

  useEffect(() => {
    const interval = setInterval(() => {
      handleRecogColor();
    }, 100);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="flex flex-col md:flex-row gap-4">
      <div className="flex flex-col">
        <video ref={videoRef} autoPlay className="rounded-md" />
        <div className="flex justify-between">
          <div className="flex my-4 bg-slate-500 px-4 rounded-md items-center justify-center gap-4 font-bold text-slate-100">
            <label className="text-xl" htmlFor="color">
              Select a Color
            </label>
            <input
              type="color"
              name="color"
              id="color"
              onChange={(e) => {
                const hex = e.target.value;
                const rgb = hex
                  .replace(
                    /^#?([a-f\d])([a-f\d])([a-f\d])$/i,
                    (m, r, g, b) => "#" + r + r + g + g + b + b
                  )
                  .substring(1)
                  .match(/.{2}/g)
                  .map((x) => parseInt(x, 16));
                setColor(rgb);
              }}
            />
          </div>
        </div>
      </div>

      {data && (
        <CapturedImage
          targetColor={{
            r: color[0],
            g: color[1],
            b: color[2],
          }}
          image={data}
        />
      )}
    </div>
  );
}

export default ColorBlockRecognition;

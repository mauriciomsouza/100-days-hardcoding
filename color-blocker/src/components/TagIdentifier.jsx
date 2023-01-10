import React, { useRef, useEffect } from "react";

const tagLib = [
  {
    name: "left",
    description:
      "This is a tag that makes the character move left, and is a red block with a white arrow pointing left.",
    image:
      "https://raw.githubusercontent.com/mauriciomsouza/coda/master/sketch/data/static/left.png",
  },
  {
    name: "right",
    description:
      "This is a tag that makes the character move right, and is a blue block with a white arrow pointing right.",
    image:
      "https://raw.githubusercontent.com/mauriciomsouza/coda/master/sketch/data/static/right.png",
  },
  {
    name: "eat",
    description:
      "This is a tag that makes the character eat, and is a green block with a white frog with the mouth open and the tongue stretched.",
    image:
      "https://raw.githubusercontent.com/mauriciomsouza/coda/master/sketch/data/static/eat.png",
  },
];

function identifyTag(pixels, tagRef) {
 return pixels
}

const TagIdentifier = ({ image }) => {
  // Cria uma referência para o elemento canvas da imagem original
  const imageRef = useRef(null);
  // Cria uma referência para o elemento canvas da imagem resultante
  const tagRef = useRef(null);

  useEffect(() => {
    // Obtém o contexto do canvas da imagem original
    const canvas = imageRef.current;
    const context = canvas.getContext("2d");
    // Cria uma nova imagem a partir da propriedade image
    var img = new Image(image);

    img.onload = function () {
      // Desenha a imagem original no canvas
      context.drawImage(img, 0, 0, 640, 480);
    };
    // Define a propriedade src da imagem como a propriedade image
    img.src = image;

    // Obtém os dados da imagem e armazena em uma matriz chamada pixels
    var imageData = context.getImageData(0, 0, 640, 480);
    var pixels = [];

    // Divide os dados da imagem em pixels individuais
    for (var i = 0; i < imageData.data.length; i += 4) {
      pixels.push({
        r: imageData.data[i],
        g: imageData.data[i + 1],
        b: imageData.data[i + 2],
        a: imageData.data[i + 3],
        id: i,
        x: (i / 4) % 640,
        y: Math.floor(i / 4 / 640),
      });
    }

    identifyTag(pixels, tagRef);
  }, [image]);

  return (
    <>
      <canvas className="hidden" ref={imageRef} width={640} height={480} />
        <canvas className="hidden" ref={tagRef} width={640} height={480} />
    </>
  );
};

export default TagIdentifier;

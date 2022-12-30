import React, { useRef, useEffect, useState } from "react";

/* Este componente recebe duas propriedades, image e targetColor,
e retorna um componente que exibe duas imagens: uma imagem original e uma imagem com blocos coloridos.

A função useRef é usada para criar referências a elementos HTML.
As referências são criadas para os elementos canvas da imagem original e da imagem resultante.
A função useEffect é um gancho do React que é executado após a renderização do componente.
Dentro da função passada para useEffect, o contexto do canvas é obtido e uma nova imagem é criada a partir da propriedade image.
O código então obtém os dados da imagem e os armazena em uma matriz chamada pixels.

O código então itera sobre os pixels e calcula a distância euclidiana entre cada pixel e a cor alvo (targetColor).
Se a distância for menor que 70, o pixel é adicionado a uma matriz chamada matchingPixels.

O código então itera sobre os pixels correspondentes e tenta agrupá-los em blocos.
Ele faz isso comparando a posição de cada pixel com a posição de todos os outros pixels correspondentes.
Se a diferença entre as coordenadas x e y de dois pixels for menor que 20, eles são considerados parte do mesmo bloco.

Por fim, o código itera sobre os blocos e desenha retângulos ao redor deles na imagem resultante.
O retângulo é desenhado usando a posição, largura e altura dos pixels no bloco. */

const CapturedImage = ({ image, targetColor }) => {
  // Cria uma referência para o elemento canvas da imagem original
  const imageRef = useRef(null);
  // Cria uma referência para o elemento canvas da imagem resultante
  const resultRef = useRef(null);

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

    let matchingPixels = [];

    // Calcula a distância entre cada pixel e a cor alvo
    for (var i = 0; i < pixels.length; i++) {
      let distance = Math.sqrt(
        Math.pow(pixels[i].r - targetColor.r, 2) +
          Math.pow(pixels[i].g - targetColor.g, 2) +
          Math.pow(pixels[i].b - targetColor.b, 2)
      );

      // Adiciona o pixel à matriz matchingPixels se a distância for menor que 70
      if (distance < 70) {
        matchingPixels.push(pixels[i]);
      }
    }

    let blocks = [];
    // Tenta agrupar os pixels correspondentes em blocos
    for (var i = 0; i < matchingPixels.length; i++) {
      if (matchingPixels[i].block === undefined) {
        let block = {
          x: matchingPixels[i].x,
          y: matchingPixels[i].y,
          width: 0,
          height: 0,
          pixels: [matchingPixels[i]],
        };

        blocks.push(block);

        matchingPixels[i].block = block;

        // Compara a posição de cada pixel com a posição de todos os outros pixels correspondentes
        for (var j = 0; j < matchingPixels.length; j++) {
          if (matchingPixels[j].block === undefined) {
            // Se a diferença entre as coordenadas x e y for menor que 20, considera os pixels parte do mesmo bloco
            if (
              Math.abs(matchingPixels[i].x - matchingPixels[j].x) < 20 &&
              Math.abs(matchingPixels[i].y - matchingPixels[j].y) < 20
            ) {
              block.pixels.push(matchingPixels[j]);
              // Armazena a referência ao bloco no pixel
              matchingPixels[j].block = block;
            }
          }
        }
      }
    }

    // Calcula a posição, largura e altura dos pixels em cada bloco
    for (var i = 0; i < blocks.length; i++) {
      let x = blocks[i].pixels[0].x;
      let y = blocks[i].pixels[0].y;

      for (var j = 0; j < blocks[i].pixels.length; j++) {
        if (blocks[i].pixels[j].x < x) {
          x = blocks[i].pixels[j].x;
        }
        if (blocks[i].pixels[j].y < y) {
          y = blocks[i].pixels[j].pixels[j].y;
        }
      }

      blocks[i].x = x;
      blocks[i].y = y;
      blocks[i].width = blocks[i].pixels[0].x - x;
      blocks[i].height = blocks[i].pixels[blocks[i].pixels.length - 1].y - y;
    }

    // Obtém o contexto do canvas da imagem resultante
    const resultCanvas = resultRef.current;
    const resultContext = resultCanvas.getContext("2d");
    // Limpa o canvas
    resultContext.clearRect(0, 0, 640, 480);
    // Desenha um retângulo ao redor de cada bloco
    for (var i = 0; i < blocks.length; i++) {
      resultContext.beginPath();
      resultContext.rect(
        blocks[i].x,
        blocks[i].y,
        blocks[i].width,
        blocks[i].height
      );
      resultContext.fillStyle = `rgba(${blocks[i].pixels[0].r}, ${blocks[i].pixels[0].g}, ${blocks[i].pixels[0].b}, ${blocks[i].pixels[0].a})`;
      resultContext.fill();
    }
  }, [image, targetColor]);

  return (
    <>
      <canvas className="hidden" ref={imageRef} width={640} height={480} />
      <canvas
      ref={resultRef} width={640} height={480} />
      </>
    );
  };
  
  export default CapturedImage;
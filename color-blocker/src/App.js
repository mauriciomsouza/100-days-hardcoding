import * as tf from '@tensorflow/tfjs';

const modelUrl = 'https://storage.googleapis.com/tfjs-models/tfjs/mobilenet_v2_1.0_224/model.json';



function App() {
  const [model, setModel] = React.useState(null);

  React.useEffect(() => {
    async function loadModel() {
      const model = await tf.loadLayersModel(modelUrl);
      setModel(model);
    }
    loadModel();
  }, []);

  return (
    <div>
      <header>
        <h1>Color Blocker</h1>
      </header>
    </div>
  );
}

export default App;

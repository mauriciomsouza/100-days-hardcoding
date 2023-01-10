import ColorBlockRecognition from "./components/ColorBlockRecognition";

function App() {
  return (
    <div className="md:mx-48">
      <header>
        <h1 className="text-4xl font-bold py-4">Color Blocker</h1>
      </header>
      <ColorBlockRecognition />
    </div>
  );
}

export default App;

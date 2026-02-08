import { useState } from "react";
import "./App.css";

function App() {
  const [topic, setTopic] = useState("Future of Artificial Intelligence");
  const [output, setOutput] = useState("");
  const [loading, setLoading] = useState(false);

  const runAgents = async () => {
    setLoading(true);
    setOutput("");

    try {
      const res = await fetch("http://localhost:8000/run", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ topic }),
      });

      const data = await res.json();
      setOutput(data.output || "No output received");

    } catch (err) {
      setOutput("Backend error. Is FastAPI running?");
    }

    setLoading(false);
  };

  return (
   <div className="container">
  <h1>Multi-Agent Research Assistant</h1>

  <div className="controls">
    <input
      value={topic}
      onChange={(e) => setTopic(e.target.value)}
      placeholder="Enter a research topic"
    />
    <button onClick={runAgents}>Run Agents</button>
  </div>

  <div className="output">
    {output || "No output yet"}
  </div>
</div>

  );
}

export default App;

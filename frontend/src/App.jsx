import { useState } from "react";
import "./App.css";

function App() {
  const [topic, setTopic] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const runAgents = async () => {
    setLoading(true);
    setResult("");

    try {
      const res = await fetch("http://localhost:8000/run", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ topic }),
      });

      const data = await res.json();
      setResult(data.final || "No output generated.");

    } catch {
      setResult("Failed to reach backend.");
    }

    setLoading(false);
  };

  return (
    <div className="app">
      <h1>Multi-Agent Research Assistant</h1>

      <div className="input-row">
        <input
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
          placeholder="Enter topic..."
        />
        <button onClick={runAgents}>
          {loading ? "Running..." : "Run Agents"}
        </button>
      </div>

      <div className="output-box">
        <pre>{result}</pre>
      </div>
    </div>
  );
}

export default App;

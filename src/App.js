import React from "react";
import BasicLayout from "./layout/BasicLayout";

function App() {
  return (
    <div className="App">
      <BasicLayout header={<h1>Hello, world!</h1>} content={"aaa"} />
    </div>
  );
}

export default App;

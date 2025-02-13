import React from 'react';
// import logo from './logo.svg';
import './App.css';
import CurrentWorkout from "./components/CurrentWorkout/CurrentWorkout.tsx"
import ClientInfo from './components/ClientInfo/ClientInfo.tsx';


function App() {
  return (
    <div className="App">
      <ClientInfo />
      <CurrentWorkout />
    </div>
  );
}

export default App;

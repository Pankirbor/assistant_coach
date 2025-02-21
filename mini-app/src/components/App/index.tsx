import React from 'react';
import CurrentWorkout from "../CurrentWorkout/CurrentWorkout.tsx"
import ClientInfo from '../ClientInfo/ClientInfo.tsx';
import { GlobalStyle } from './styles.tsx';


function App() {
  return (
    <React.Fragment>
      <GlobalStyle />
      <ClientInfo />
      <CurrentWorkout />
    </React.Fragment>
  );
}

export default App;

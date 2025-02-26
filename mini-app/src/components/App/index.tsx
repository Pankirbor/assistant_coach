import React from 'react';
// import CurrentWorkout from "../CurrentWorkout/CurrentWorkout.tsx"
// import ClientInfo from '../pages/ClientInfoPage/ClientInfo.tsx';
import { GlobalStyle } from './styles.tsx';
import {PageWrapper} from '../layout/PageWrapper/index.tsx';


function App() {
  return (
    <React.Fragment>
      <GlobalStyle />
      {/* <ClientInfo /> */}
      <PageWrapper>Content</PageWrapper>
    </React.Fragment>
  );
}

export default App;

import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './components/App/index.tsx';
import { ThemeProvider } from 'styled-components';
import { defaultTheme } from './themes/default.ts';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <React.StrictMode>
    <ThemeProvider theme={defaultTheme}>
      <App />
    </ThemeProvider>
  </React.StrictMode>
);

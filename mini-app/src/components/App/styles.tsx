import {createGlobalStyle} from "styled-components"

export const GlobalStyle = createGlobalStyle`
    html {
        height: 100%;
    }

    body,
    html {
        margin: 0;
    }

    body {
        position: relative;
        min-height: 100%;
        font-family: "Inter", "Arial", sans-serif;
        font-size: 14px;
        line-height: 27px;
        font-weight: 400;
        color: #333333;
    }
`
import styled from "styled-components";

interface StyledButtonProps {
    $maxWidth?: string;
}

export const StyledButton = styled.a<StyledButtonProps>`
    display: block;
    min-height: 60px;
    padding: 0 15px;
    max-width: 100px;
    min-width: ${(props) => props.$maxWidth ? "100%" : "50px"};
    font-size: ${(props) => props.theme.fontSizeDefault};
    font-weight: bold;
    line-height: 58px;
    text-align: center;
    text-decoration: none;
    color: ${(props) => props.theme.colorWhite};
    background-color: ${(props) => props.theme.buttonColor};
    border: none;
    background-image: none;
    box-shadow: none;
    cursor: pointer;
    transition: background-color 0.2s ease-out, box-shadow 0.2s ease-out;
    box-sizing: border-box;
    font-family: ${(props) => props.theme.fontFamily};

    &:hover,
    &:active {
        background-color: ${(props) => props.theme.buttonColorHoverActive};
        box-shadow: inset 0 4px 0 rgba(0, 0, 0, 0.14);
    }

    &:active {
        box-shadow: none;
    }

    &:disabled {
        opacity: 0.5;
        box-shadow: none;
        background-color: ${(props) => props.theme.buttonColor};
    }
`;

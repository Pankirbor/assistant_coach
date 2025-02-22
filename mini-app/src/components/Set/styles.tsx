import styled from "styled-components";
import {PageItemWrapper as SetItemWrapper} from "../helpers/PageItemWrapper.tsx";

interface SetInputsProps {
    $width?: string
}

export const SetInput = styled.input<SetInputsProps>`
    width: ${(props)=> props.$width ? props.$width : "100px"};
    padding: 10px;
    font-size: ${(props)=>props.theme.fontSizeDefault};
    border: none;
    /* border-color: ${(props)=>props.theme.backgroundColorBlue}; */
    border-radius: 8px;
    background-color: ${(props)=>props.theme.inputBackgroundColor};
    color: ${(props)=>props.theme.fontColorBlack};
    outline: none;
    transition: border-color 0.3s ease, box-shadow 0.3s ease;
    margin-right: 10px;
    margin-bottom: 5px;

    &:focus {
        /* border-color: ${(props)=>props.theme.backgroundColorBlueDark}; */
        box-shadow: 0 0 5px rgba(127, 140, 141, 0.5)
    }

    &::placeholder {
        color: ${(props)=>props.theme.backgroundColorGray};
    }
`
export const Wrapper = styled(SetItemWrapper)`
    display: flex;
    flex-direction: ${(props)=>props.flexDirection ? props.flexDirection : "column"};
    align-items: ${(props)=>props.alignItems ? props.alignItems: "flex-start"};
`
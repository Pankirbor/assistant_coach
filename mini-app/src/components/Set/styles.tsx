import styled, { css } from "styled-components";
import {PageItemWrapper as SetItemWrapper} from "../helpers/PageItemWrapper.tsx";

interface Props {
    $width?: string;
    $label?: boolean;
    $isWeight?: boolean;
}


export const SetInput = styled.input<Props>`
    width: ${(props)=> props.$width ? props.$width : "100px"};
    padding: 10px;
    /* padding-right: ${(props)=> props.$isWeight ? "16px" : "10px"}; */
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
    position: relative;

    &:focus {
        /* border-color: ${(props)=>props.theme.backgroundColorBlueDark}; */
        box-shadow: 0 0 5px rgba(127, 140, 141, 0.5)
    }

    &::placeholder {
        color: ${(props)=>props.theme.backgroundColorBlue};
    }

`
export const Wrapper = styled(SetItemWrapper)`
    display: flex;
    flex-direction: ${(props)=>props.flexDirection ? props.flexDirection : "column"};
    align-items: ${(props)=>props.alignItems ? props.alignItems: "flex-start"};
    position: relative;
`

export const KgLabel = styled.span<{right?: string}>`
        position: absolute;
        right: ${(props) => props.right ? props.right : "30px"};
        top: 50%;
        transform: translateY(-60%);
        font-size: 14px;
        pointer-events: none;
`

const setLabel =  css`
                &::before {
                    content: "🎯";
                    display: inline-block;
                    width: 20px;
                    height: 20px;
                    position: absolute;
                    top: 0;
                    left: 0;
                }
        `

export const SetText = styled.span<Props>`
    display: inline-block;
    color: ${(props) => props.theme.fontColorBlack};
    font-size: ${(props)=>props.theme.fontSizeDefault};
    padding: 0px 10px;
    padding-left: ${(props)=> props.$label ? "35px" : "10px"};
    /* border: 1px solid green; */
    width: ${(props)=> props.$width ? props.$width : "100px"};
    margin-right: ${(props)=> props.$label ? "15px" : "0px"};
    margin-bottom: 5px;
    margin-left: ${(props)=> props.$label ? "-22px" : "25px"};
    position: relative;
    text-align: left;
    ${(props)=> props.$label && setLabel}
`
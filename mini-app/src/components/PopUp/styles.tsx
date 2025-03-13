import styled from "styled-components";
import { Button } from "../ui/Button/index.tsx";

export const Wrapper = styled.div`
    border: 1px solid black;
    padding: 15px;
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    min-width: 300px;
    z-index: 100;
    background-color: #fff;
    border-radius: 15px;
`

export const Close = styled(Button)`
    position: absolute;
    top: 0;
    right: 5px;
    min-width: 30px;
    min-height: 30px;
    border-radius: 50%;
    line-height: 1;
`

export const Header = styled.header`
    position: relative;
    padding: 5px 0;
    display: flex;
    border-bottom: ${(props)=> `1px solid ${props.theme.backgroundColorBlueDark}`};
    margin-bottom: 10px;
    font-size: 16px;
    font-weight: bold;
`
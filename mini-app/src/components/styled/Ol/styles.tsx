import styled from "styled-components"

export const Ol = styled.ol<{$bottom?: string}>`
    padding: 0;
    margin-bottom: ${(props)=> props.$bottom ? props.$bottom : "10px"};
`
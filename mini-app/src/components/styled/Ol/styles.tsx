import styled from "styled-components"

export const Ol = styled.ol<{$bottom?: string}>`
    /* list-style: square; */
    /* font: 15px 'trebuchet MS', 'lucida sans'; */
    padding: 0;
    margin-bottom: ${(props)=> props.$bottom ? props.$bottom : "10px"};
`
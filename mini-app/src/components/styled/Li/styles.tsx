import styled from "styled-components";

interface LiProps {
  $borderTop?: boolean;
}

export const Li = styled.li<LiProps>`
  /* list-style: none; */
  vertical-align: top;
  border-top: ${(props)=> props.$borderTop ? ` 1px solid ${props.theme.backgroundColorBlueDark}` : ""}
  /* border-top-color: ${(props)=> props.$borderTop ? props.theme.backgroundColorBlueDark : ""}; */
`;

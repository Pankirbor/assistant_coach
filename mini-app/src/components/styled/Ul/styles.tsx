import styled, { css } from "styled-components";

interface UlProps {
    $indent?: string;
    $align?: string;
    $fontSize?: string;
    $lineHeight?: string;
    $isGridList?: boolean;
}

const gridList = css<UlProps>`
  margin-left: ${(props) =>
    props.$indent ? `-${props.$indent}px` : `-${props.theme.indent}`};
  margin-top: ${(props) =>
    props.$indent ? `-${props.$indent}px` : `-${props.theme.indent}`};
  font-size: 0;
  line-height: 0;
  text-align: ${(props) => props.$align || "center"};

  li {
    display: inline-block;
    margin-left: ${(props) =>
      props.$indent ? `${props.$indent}px` : props.theme.indent};
    margin-top: ${(props) =>
      props.$indent ? `${props.$indent}px` : props.theme.indent};
    font-size: ${(props) =>
      props.$fontSize ? `${props.$fontSize}px` : props.theme.fontSizeDefault};
    line-height: ${(props) =>
      props.$lineHeight ? `${props.$lineHeight}px` : "27px"};
    vertical-align: top;
  }
`;

export const Ul = styled.ul<UlProps>`
  margin: 0;
  padding: 0;
  list-style: none;
  ${(props) => (props.$isGridList ? gridList : "")}
`;
import styled from "styled-components";

export const Section = styled.section`
  position: relative;
  display: flex;
  padding-top: 10px;
  padding-bottom: 10px;
  padding-left: ${(props) => props.theme.pagePadding};
  padding-right: ${(props) => props.theme.pagePadding};
  box-sizing: border-box;
`;

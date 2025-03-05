import styled from "styled-components";

export const Section = styled.section`
  position: relative;
  display: flex;
  padding: 10px;
  padding-bottom: 10px ${(props) => props.theme.pagePadding};
  box-sizing: border-box;
`;

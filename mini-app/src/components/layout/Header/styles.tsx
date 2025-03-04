import styled from "styled-components";
import { Section } from "../../styled/index.tsx";

export const StyledHeader = styled(Section)`
  position: relative;
  width: 327px;
  margin: 0 auto;
  height: 80px;
  padding-top: 0;
  padding-bottom: 0;
  justify-content: space-evenly;
  background-color: ${(props) => props.theme.colorWhite};
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.04), 0 0 2px rgba(0, 0, 0, 0.06),
    0 0 1px rgba(0, 0, 0, 0.04);
  align-items: center;
  z-index: 5;
  margin-bottom: 30px;
`;
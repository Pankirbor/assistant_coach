import styled, { css } from "styled-components"

export const TitleSize = {
  BIG: "big",
  MEDIUM: "medium",
  SMALL: "small",
  EXTRA_SMALL: "extra_small"
};

const TitleSizeValue = {
  [TitleSize.BIG]: {
    fontSize: "24px",
    lineHeight: "30px"
  },
  [TitleSize.MEDIUM]: {
    fontSize: "18px",
    lineHeight: "24px"
  },
  [TitleSize.SMALL]: {
    fontSize: "14px",
    lineHeight: "21px"
  },
  [TitleSize.EXTRA_SMALL] : {
    fontSize: "12px",
    lineHeight: "20px",
  },
}

interface TitleProps {
    marginBottom?: string;
    size?: string;
}

export const Title = styled.h1<TitleProps>`
  margin: 0;
  padding: 0;
  margin-bottom: ${(props) => props.marginBottom || 0}px;
  font-weight: bold;
  ${(props) => {
    const values = TitleSizeValue[props.size || TitleSize.MEDIUM];
    return css`
      font-size: ${values.fontSize};
      line-height: ${values.lineHeight};
    `;
  }};
`;

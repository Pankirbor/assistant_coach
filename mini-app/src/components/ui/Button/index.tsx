import React from "react";
import { StyledButton } from "./styles.tsx";

interface Props {
    children?: string;
    link?: string;
    maxWidth?: string;
    className?: string;
    onClick?: (event: React.MouseEvent<HTMLButtonElement>) => void;
}

export const Button:React.FC<Props> = ({
    children,
    link,
    maxWidth,
    className,
    onClick,
    ...props
}) => {
    return (
    <StyledButton
      {...props}
      $maxWidth={maxWidth}
      {...(link ? { to: link } : { as: "button", onClick, type: "button" })}
      className={className}
    >
      {children}
    </StyledButton>
  );
}
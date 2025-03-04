import React from "react";
import { Button } from "../../ui/Button/index.tsx";
import { Title } from "../../ui/Title/styles.tsx";
import { StyledHeader } from "./styles.tsx";

export const Header = ({title}) => {
    return (
        <>
        <StyledHeader>
            <Button > X</Button>
            <Title>{ title }</Title>
        </StyledHeader>
        </>
    )
}
import React, { ReactNode } from "react";
import { Wrapper, Header, Close } from "./styles.tsx";

interface PopUpProps {
    isShow: boolean;
    onClose: () => void;
    title?: string;
    children: ReactNode;
}
export const PopUp:React.FC<PopUpProps> = ({isShow, onClose, title, children}) => {
    return isShow ? (
        <Wrapper>
            <Header>
                {title}{" "}
                <Close onClick={onClose}>X</Close>
            </Header>
            {children}
        </Wrapper>
    ) : null;
}
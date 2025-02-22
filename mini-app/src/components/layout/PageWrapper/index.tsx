import React, { ReactNode } from "react";
// import Header from "/src/components/layout/header/header";
// import Footer from "/src/components/layout/footer/footer";
// import MainPage from "/src/components/pages/main-page/main-page";
import { Main } from "./styles.tsx";
import { CurrentWorkoutPage } from "../../pages/CurrentWorkoutPage/index.tsx";

interface Props {
    children: ReactNode;
    features?: ReactNode;
}

export const PageWrapper:React.FC <Props> = ({ children, features }) => {
  return (
    <>
      {/* <Header /> */}
      <Main>
        <CurrentWorkoutPage />
      </Main>
      {/* <Footer /> */}
    </>
  );
}

export default PageWrapper;
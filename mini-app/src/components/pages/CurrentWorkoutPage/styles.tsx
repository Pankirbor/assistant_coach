import styled from "styled-components";
import { Ol, Section } from "../../styled/index.tsx";
import {PageItemWrapper as WorkoutItemWrapper} from "../../helpers/PageItemWrapper.tsx";


export const Workout = styled(Section)`
    border: 1px solid;
    border-color: ${(props)=> props.theme.backgroundColorBlueDark};
    border-radius: 8px;
    background-color: ${(props)=> props.theme.colorWhite};
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin-top: 50px;
    flex-direction: column;
    align-items: center;
`

export const Wrapper = styled(WorkoutItemWrapper)`
    display: flex;
    flex-direction: ${(props)=>props.flexDirection ? props.flexDirection : "column"};
    align-items: ${(props)=>props.alignItems ? props.alignItems: "flex-start"};
`
interface TitleExerciseButtonProps {
    isActive?: boolean;
    onClick?: () => void;
}

export const TitleExerciseButton = styled.button<TitleExerciseButtonProps>`
    width: 100%;
    text-align: left;
    padding-top: 10px;
    padding-bottom: 10px;
    padding-left: 20px;
    padding-right: 20px;
    border: none;
  cursor: ${(props) => (props.isActive ? "auto" : "pointer")};
    box-shadow: none;
    display: block;
    font-size: 16px;
    background-color: ${(props)=>props.theme.colorWhite};

    &:after {
        content: '\002B';
        color: #777;
        font-weight: bold;
        float: right;
        /* margin-left: 5px; */
    }
`
export const ExerciseSetsOl = styled(Ol)`
    position: relative;
    /* border: 1px solid green; */
    height: 0px;
    overflow: hidden;
    word-wrap: 100%;
    transition: 0.4s;
`

export const Content = styled.div`
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  /* border: 1px solid #ddd; */
  padding: ${(props) => props.theme.indent};
  line-height: 1.5;
  font-size: 16px;
  box-sizing: border-box;
  text-align: left;
`;
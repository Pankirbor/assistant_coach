import styled from "styled-components";
import { Ol, Section } from "../../styled/index.tsx";
import {PageItemWrapper as WorkoutItemWrapper} from "../../helpers/PageItemWrapper.tsx";
import { Button as WorkoutButton } from "../../ui/Button/index.tsx";
import arrowIcon from "../../../assets/images/arrowIcon.svg"

export const StyledWorkoutButton = styled(WorkoutButton)`
    border-radius: 99px;
    /* padding: 10px; */
    width: 178px;
    /* height: 46px; */
    box-shadow: 0 10px 22px 0 rgba(149, 173, 254, 0.3);
    background-color: ${(props) =>`linear-gradient(317deg, ${props.theme.buttonColor} 0%, #9dceff 100%)`};
`


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
    isOpen?: boolean;
    onClick?: () => void;
}

export const TitleExerciseButton = styled.button<TitleExerciseButtonProps>`
    position: relative;
    min-width: 327px;
    text-align: left;
    padding-top: 10px;
    padding-bottom: 10px;
    padding-left: 20px;
    padding-right: 20px;
    border: none;
    cursor: ${(props) => (props.isOpen ? "auto" : "pointer")};
    box-shadow: none;
    display: flex;
    font-size: 16px;
    background-color: ${(props)=>props.theme.colorWhite};
    box-sizing: border-box;

    &::after {
        position: absolute;
        top: 20px;
        right: 15px;
        content: ' ';
        color: #777;
        font-weight: bold;
        float: right;
        width: 5px;
        height: 8px;
        /* background-color: green; */
        margin: auto;
        background-image: url(${arrowIcon});
        background-repeat: no-repeat;
        transform: ${(props)=> props.isOpen ? "rotate(-90deg)" : "rotate(90deg)"};
        transition: transform 0.2s;
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
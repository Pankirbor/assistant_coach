import styled from "styled-components";
import { Ol, Section } from "../../styled/index.tsx";
import {PageItemWrapper as WorkoutItemWrapper} from "../../helpers/PageItemWrapper.tsx";
import { Button as WorkoutButton } from "../../ui/Button/index.tsx";
import arrowIcon from "../../../assets/images/arrowIcon.svg"

export const StyledWorkoutButton = styled(WorkoutButton)<{$width?:string, $radius?: string, disabled?: boolean}>`
    border-radius: ${(props) => props.$radius ? props.$radius: "20px"};
    width: ${(props)=> props.$width ? props.$width : "178px"};
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

export const Wrapper = styled(WorkoutItemWrapper)<{$width?:string}>`
    display: flex;
    flex-direction: ${(props)=>props.flexDirection ? props.flexDirection : "column"};
    align-items: ${(props)=>props.alignItems ? props.alignItems: "flex-start"};
`

export const WrapperButtons = styled(Wrapper)`
    justify-content: space-evenly;
    margin: 10px 10px;
`

export const WarmCard = styled(Wrapper)`
    margin-bottom: 15px;
    border-radius: 15px;
    padding: 5px 10px;
    width: 250px;
    background: linear-gradient(135deg, #FF617A, #FF8093);
    box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.5);
    font-size: 12px;
`
interface TitleExerciseButtonProps {
    isOpen?: boolean;
    onClick?: () => void;
}

export const TitleExerciseButton = styled.button<TitleExerciseButtonProps>`
    position: relative;
    min-width: 327px;
    text-align: left;
    padding: 10px 20px;
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
        margin: auto;
        background-image: url(${arrowIcon});
        background-repeat: no-repeat;
        transform: ${(props)=> props.isOpen ? "rotate(-90deg)" : "rotate(90deg)"};
        transition: transform 0.2s;
    }
`
export const ExerciseSetsOl = styled(Ol)`
    position: relative;
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
  padding: ${(props) => props.theme.indent};
  line-height: 1.5;
  font-size: 16px;
  box-sizing: border-box;
  text-align: left;
`;
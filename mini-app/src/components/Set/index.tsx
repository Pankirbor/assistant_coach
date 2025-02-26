import React from "react";
import { SetInput, SetText, Wrapper } from "./styles.tsx";

interface SetResultProps {
  actual_weight: number | string;
  actual_reps: number | string;
}

interface SetReadProps {
  targetWeight: number | string;
  targetReps: number | string;
}


interface SetProps {
  exerciseId: number;
  set: SetResultProps;
  setIndex: number;
  onSetChange: (exerciseId: number, setIndex: number, field: string, value: string) => void;
}

export const Set:React.FC <SetProps> = ({exerciseId, set, setIndex, onSetChange}) => {
    return (
        <Wrapper flexDirection="row" alignItems="center">
            <SetInput
                type="number"
                placeholder="Вес"
                value={set.actual_weight || " "}
                onChange={(e)=>{onSetChange(exerciseId, setIndex, "actual_weight", e.target.value)}}
            />
            <SetInput
                $width="70px"
                type="number"
                placeholder="Кол-во"
                value={set.actual_reps || " "}
                onChange={(e)=>{onSetChange(exerciseId, setIndex, "actual_reps", e.target.value)}}
            />

        </Wrapper>
    )
}

export const SetRead:React.FC <SetReadProps> = ({targetWeight, targetReps}) => {
    return (
        <Wrapper flexDirection="row" alignItems="center">
            <SetText $label> {targetWeight} кг</SetText>
            <SetText $width="70px"> {targetReps} раз(а)</SetText>
        </Wrapper>
    )
}
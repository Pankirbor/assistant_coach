import React, { useState } from "react";
import { KgLabel, SetInput, SetText, Wrapper } from "./styles.tsx";

interface SetResultProps {
    target_weight?: string;
    terget_reps?: number;
    actual_weight: string | number;
    actual_reps: string |number;
    comment?: string,
    is_last?: boolean;
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
    const [weight, setWeight] = useState(set.target_weight);

    const handleSetWeight = (event) => {
        setWeight(event.target.value);
        onSetChange(exerciseId, setIndex, "actual_weight", event.target.value)
    }
    return (
        <Wrapper flexDirection="row" alignItems="center">
            <Wrapper flexDirection="row">
                <SetInput
                    type="number"
                    value={weight}
                    onChange={handleSetWeight}
                    $isWeight
                />
                <KgLabel>кг</KgLabel>
            </Wrapper>
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
            <Wrapper flexDirection="row">
                <SetText $label $width="60px"> {targetWeight}</SetText>
                <KgLabel right="-2px">кг</KgLabel>
            </Wrapper>
            <SetText $width="80px"> {targetReps}-{targetReps}  раз(а)</SetText>
        </Wrapper>
    )
}
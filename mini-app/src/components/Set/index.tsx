import React, { ReactNode } from "react";
import { SetInput, Wrapper } from "./styles.tsx";

interface Set {
  actual_weight: number | string;
  actual_reps: number | string;
}

interface Exercise {
    id: number;
    exercise_id: number;
    name: string;
    video_link: string;
    timing: string;
    target_weight: number;
    target_reps: number;
    target_sets: number;
    general_order: number;
    is_done: boolean;
    comment: string;
    client_comment: string;
    best_result: string;
    results: Set[]
}

interface SetProps {
  exercise: Exercise;
  set: Set;
  setIndex: number;
  onSetChange: (exerciseId: number, setIndex: number, field: keyof Set, value: string) => void;
}

export const Set:React.FC <SetProps> = ({exercise, set, setIndex, onSetChange}) => {
    return (
        <Wrapper flexDirection="row" alignItems="center">
            <SetInput
                type="number"
                placeholder="Вес"
                value={set.actual_weight || " "}
                onChange={(e)=>{onSetChange(exercise.id, setIndex, "actual_weight", e.target.value)}}
            />
            <SetInput
                $width="70px"
                type="number"
                placeholder="Повторения"
                value={set.actual_reps || " "}
                onChange={(e)=>{onSetChange(exercise.id, setIndex, "actual_reps", e.target.value)}}
            />

        </Wrapper>
    )
}
import axios from "axios";
import React, { useEffect, useState } from "react";
import { Title } from "../../ui/Title/styles.tsx";
import { Workout, Wrapper, StyledWorkoutButton, WarmCard } from "./styles.tsx";
import Accordion from "../../Accordion/index.tsx";
// import { Header } from "../../layout/Header/index.tsx";
import type { WorkoutProps, ExerciseProps, ExerciseResultProps, TrainingSegmentsProps} from "../../../types/data/dataTypes.ts";
import { P } from "../../styled/index.tsx";



export const CurrentWorkoutPage:React.FC= () => {
    const [workout, setWorkout] = useState<WorkoutProps | null>(null);
    const [results, setResults] = useState<ExerciseResultProps[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    // Загрузка текущей тренировки
    useEffect(() => {
        const fetchWorkout = async () => {
        try {
            const response = await axios.get("/api/workouts/2");
            setWorkout(response.data);
            initializeResults(response.data.training_segments.map((segment:TrainingSegmentsProps) => segment.exercises).flat());
        } catch (err) {
            setError(`Не удалось загрузить тренировку ${err}`);

        } finally {
            setLoading(false);
        }
        };

        fetchWorkout();
    }, []);

    useEffect(()=>{
      console.log(workout)
      console.log("workout")
    });

    // Инициализация структуры для результатов
    const initializeResults = (exercises: ExerciseProps[]) => {
        const initialResults = exercises.map((exercise) => ({
        exerciseId: exercise.id,
        sets: Array(exercise.target_sets).fill(
          {
            target_weight: exercise.target_weight,
            terget_reps: exercise.target_sets,
            comment: "",
            is_last: false,
            actual_weight: 0,
            actual_reps: 0
          }
        ),
        }));
        setResults(initialResults);
    };

    // Обработчик изменения данных подхода
    const handleSetChange = (
      exerciseId: number,
      setIndex: number,
      field: string,
      value: string
    ) => {
      setResults((prevResults) =>
        prevResults.map((exerciseResult) => {
          if (exerciseResult.exerciseId === exerciseId) {
            const newSets = [...exerciseResult.sets];
            newSets[setIndex] = {
              ...newSets[setIndex],
              [field]: Number(value), //* добавить обработку для is_last
            };
            return { ...exerciseResult, sets: newSets };
          }
          return exerciseResult;
        })
      );
    };

    //* Отправка результатов
    const handleSubmit = async () => {
      if (!workout) return;

      try {
        // await axios.put(`/api/workout/${workout.id}`, {
        //   results: results,
        // });
        console.log({results: results})
        alert(`${JSON.stringify({results: results})}` );
      } catch (err) {
        setError("Ошибка при сохранении результатов");
      }
    };

    if (loading) return <div>Загрузка...</div>;
    if (error) return <div>{error}</div>;
    if (!workout) return <div>Нет активных тренировок</div>;
    alert(`${JSON.stringify(workout)}` );

    const items = workout.training_segments.map((segment) => segment.exercises.map((exercise: ExerciseProps, index) => {
                      return {
                        title: exercise.name,
                        content: {...results[index], "targetWeight": exercise.target_weight, "targetReps": exercise.target_reps},
                        onSetChange: handleSetChange,
                      }
                    })).flat();

    return (
        <>
            <Workout>
              {/* <Header title={"Current Workout"}/> */}
              <Wrapper>
                <Title marginBottom="30" size="big">{workout.tags.map((tag) => tag.name).join(", ")}</Title>
                <WarmCard>
                  <P>Необходимо сделать два разминочных подхода:</P>
                  <P>1. 25% от рабочего веса</P>
                  <P>2. 50% от рабочего веса</P>
                </WarmCard>
                <Wrapper>
                  <Accordion items={items} />
                </Wrapper>
              </Wrapper>
                <StyledWorkoutButton onClick={handleSubmit}>Завершить</StyledWorkoutButton>
            </Workout>
        </>
    )
}
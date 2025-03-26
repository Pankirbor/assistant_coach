import axios from "axios";
import React, { useEffect, useState, useMemo } from "react";
import { Title } from "../../ui/Title/styles.tsx";
import { Workout, Wrapper, WrapperButtons, StyledWorkoutButton, WarmCard } from "./styles.tsx";
import Accordion from "../../Accordion/index.tsx";
import type { WorkoutProps, ExerciseProps, ExerciseResultProps, TrainingSegmentsProps} from "../../../types/data/dataTypes.ts";
import { P } from "../../styled/index.tsx";
import { PopUp } from "../../PopUp/index.tsx";
import InfoIcon from '@mui/icons-material/Info';
import { IconButton } from "@mui/material";

export const WellDoneOrNeedToFinish:React.FC<{isWellDone: boolean, onClick:()=>void}> = ({isWellDone, onClick}) => {
    return (
        <>
        {isWellDone ? <P>Поздравляю, вы хорошо познимались. Закончить тренировку?</P>
        : <P>У вас остались незаполненные поля, вы уверены, что хотите закончить тренировку?</P>}
        <WrapperButtons flexDirection="row" alignItems="center" $width="200px">
          <StyledWorkoutButton onClick={onClick} $width="70px">Yes</StyledWorkoutButton>
          <StyledWorkoutButton onClick={onClick}  $width="70px">No</StyledWorkoutButton>
        </WrapperButtons>
        </>
  )
}


export const CurrentWorkoutPage:React.FC= () => {
    const [workout, setWorkout] = useState<WorkoutProps | null>(null);
    const [results, setResults] = useState<ExerciseResultProps[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");
    const [isShowPopUp, setIsShowPopUp] = useState(false);
    const [isWellDone, setIsWellDone] = useState(true);
    const [isShowWarm, setIsShowWarm] = useState(false);
    const [telegramId, setTelegramId] = useState<string | null>(null);

    useEffect(() => {
        const queryParams = new URLSearchParams(window.location.search);
        console.log(`LOG ${queryParams.get('telegramId')}`)
        const tgid = queryParams.get('telegramId');
        if (tgid) {
            setTelegramId(tgid);
        }
    }, []);

    //Загрузка текущей тренировки
    useEffect(() => {

        if (!telegramId) return; // не делаем запрос если ID не установлен
        const fetchWorkout = async () => {
        try {
            const response = await axios.get(`/api/workouts/next_workout/?telegram_id=${telegramId}`);
            setWorkout(response.data);
            initializeResults(response.data.training_segments.map((segment:TrainingSegmentsProps) => segment.exercises).flat());
        } catch (err) {
            setError(`Не удалось загрузить тренировку ${err}`);

        } finally {
            setLoading(false);
        }
        };

        fetchWorkout();
    }, [telegramId,]);

//! Отладочная информация
    // useEffect(()=>{
    //   console.log(workout)
    //   console.log("workout")
    // });

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
            actual_weight: exercise.target_weight,
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
            return { ...exerciseResult, sets: newSets};
          }
          return exerciseResult;
        })
      );
    };

    //* Отправка результатов
    const handleSubmit = async () => {
      if (!workout) return;

      try {
        const finalResult = results.reduce((acc, result) => {
          acc.set(result.exerciseId, result.sets)
          return acc
        }, new Map())

        for (const key of finalResult.keys()) {
          if (finalResult.get(key).some((value)=> Boolean(value.actual_reps) === false)) {
            setIsWellDone(false)
            break
          }
        }

        workout.training_segments.forEach(segment => {
          segment.exercises.forEach(
            exersice => {
              exersice.results = [...finalResult.get(exersice.id)]
            }
          );
        });

        const response = await axios.put(`/api/workouts/${workout.id}/`, {
          ...workout,
        });
        console.log('Данные обновлены:', response.data);

        console.log(finalResult);
        console.log(JSON.stringify(workout));
        setIsShowPopUp(true);
      } catch (err) {
        console.error('Ошибка при обновлении:', error);
        setError("Ошибка при сохранении результатов");
      }
    };

    const items = useMemo(() => {
      if (!workout) {
        return [];
      }

      return workout.training_segments
        .map((segment) => segment.exercises
          .map((exercise: ExerciseProps, index) => {
                return {title: exercise.exercise.name,
                        content: {...results[index], "targetWeight": exercise.target_weight, "targetReps": exercise.target_reps},
                        onSetChange: handleSetChange,
                      }
                })
        )
        .flat();
    }, [workout, results, handleSetChange]);

    if (loading) return <div>Загрузка...</div>;
    if (error) return <div>{error}</div>;
    if (!workout) return <div>Нет активных тренировок</div>;


    return (
        <>
            <Workout>
              <Wrapper>
                <Title marginBottom="30" size="big">
                  {workout.tags.map((tag) => tag.name).join(", ")}
                  <IconButton onClick={() => setIsShowWarm((isShowWarm)=> !isShowWarm)} aria-label="info">
                    <InfoIcon />
                  </IconButton>
                </Title>
                <PopUp title="Разминка" isShow={isShowWarm} onClose={() => setIsShowWarm(false)}>
                  <WarmCard>
                    <P>Необходимо сделать два разминочных подхода:</P>
                    <P>1. 25% от рабочего веса</P>
                    <P>2. 50% от рабочего веса</P>
                  </WarmCard>
                </PopUp>
                <Wrapper>
                  <Accordion items={items} />
                </Wrapper>
              </Wrapper>
              <StyledWorkoutButton disabled={isShowPopUp} onClick={handleSubmit}>Завершить</StyledWorkoutButton>
              <PopUp isShow={isShowPopUp} onClose={() => setIsShowPopUp(false)} title="Завершение тренировки">
                <WellDoneOrNeedToFinish onClick={() => setIsShowPopUp(false)} isWellDone={isWellDone}/>
              </PopUp>
            </Workout>
        </>
    )
}
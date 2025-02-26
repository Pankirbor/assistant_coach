import axios from "axios";
import React, { useEffect, useState } from "react";
import { Title } from "../../ui/Title/styles.tsx";
import { Workout, Wrapper, StyledWorkoutButton } from "./styles.tsx";
import Accordion from "../../Accordion/index.tsx";

//* Типы для данных клиента
interface ClientProps {
  id: number;
  telegram_id: number;
  username: string;
  first_name: string;
  last_name: string;
  email: string;
}

interface TagProps {
      id: number;
      name: string;
      slug: string;
}

interface SetProps {
    target_weight?: string;
    terget_reps?: number;
    actual_weight: string | number;
    actual_reps: string | number;
    comment?: string,
    is_last?: boolean;
}

interface ExerciseProps {
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
    results: SetProps[]
}

interface TrainingSegmentsProps {
      timing: string;
      is_circle: boolean;
      number_laps: number;
      exercises: ExerciseProps[];

}

interface WorkoutProps {
  id: number;
  date: string;
  client: ClientProps;
  tags: TagProps[];
  timing: string;
  training_segments: TrainingSegmentsProps[]
}

interface ExerciseResultProps {
  exerciseId: number;
  sets: SetProps[];
}

export const CurrentWorkoutPage:React.FC= () => {
    const [workout, setWorkout] = useState<WorkoutProps | null>(null);
    const [results, setResults] = useState<ExerciseResultProps[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    // Загрузка текущей тренировки
    useEffect(() => {
        const fetchWorkout = async () => {
        try {
            const response = await axios.get("/api/workouts/3");
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

    // Инициализация структуры для результатов
    const initializeResults = (exercises: ExerciseProps[]) => {
        const initialResults = exercises.map((exercise) => ({
        exerciseId: exercise.id,
        sets: Array(exercise.target_sets).fill({ actual_weight: 0, actual_reps: 0 }),
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
              [field]: Number(value),
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
        await axios.put(`/api/workout/${workout.id}`, {
          results: results,
        });
        alert("Результаты успешно сохранены!");
      } catch (err) {
        setError("Ошибка при сохранении результатов");
      }
    };

    if (loading) return <div>Загрузка...</div>;
    if (error) return <div>{error}</div>;
    if (!workout) return <div>Нет активных тренировок</div>;

    const items = workout.training_segments.map((segment) => segment.exercises.map((exercise, index) => {
                      return {
                        title: exercise.name,
                        content: results[index],
                        onSetChange: handleSetChange,
                      }
                    })).flat();

    return (
        <>
            <Workout>
                <Title marginBottom="30" size="big">{workout.tags.map((tag) => tag.name).join(", ")}</Title>
                <Wrapper>
                  <Accordion items={items} />
                </Wrapper>
                <StyledWorkoutButton >Завершить</StyledWorkoutButton>
            </Workout>
        </>
    )
}
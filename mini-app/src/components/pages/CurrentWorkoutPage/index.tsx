import axios from "axios";
import React, { useEffect, useRef, useState } from "react";
import { Title } from "../../ui/Title/styles.tsx";
import { ExerciseSetsOl, Workout, Wrapper, Content } from "./styles.tsx";
import { Ol, Li, Ul } from "../../styled/index.tsx";
import { Set } from "../../Set/index.tsx";
import { TitleExerciseButton } from "./styles.tsx";

//* Типы для данных клиента
interface Client {
  id: number;
  telegram_id: number;
  username: string;
  first_name: string;
  last_name: string;
  email: string;
}

interface Tag {
      id: number;
      name: string;
      slug: string;
}

interface Set {
    target_weight?: string;
    terget_reps?: number;
    actual_weight: string;
    actual_reps: number;
    comment?: string,
    is_last?: boolean;
}

interface SetForm {
    target_weight: string;
    terget_reps: number;
    actual_weight: string;
    actual_reps: number;
    comment: string,
    is_last: boolean;
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

interface TrainingSegments {
      timing: string;
      is_circle: boolean;
      number_laps: number;
      exercises: Exercise[];

}

interface Workout {
  id: number;
  date: string;
  client: Client;
  tags: Tag[];
  timing: string;
  training_segments: TrainingSegments[]
}

interface ExerciseResult {
  exerciseId: number;
  sets: {
    actual_weight: number;
    actual_reps: number;
  }[];
}

export const CurrentWorkoutPage:React.FC= () => {
    const [workout, setWorkout] = useState<Workout | null>(null);
    const [results, setResults] = useState<ExerciseResult[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");
    const [activeIndex, setActiveIndex] = useState(0);
    const [height, setHeight] = useState(0)
    const openContent = useRef<HTMLDivElement | null>(null)

    useEffect(() => {
      if (openContent.current){
        setHeight(openContent.current.offsetHeight);
      }
    }, [height, activeIndex])


    // Загрузка текущей тренировки
    useEffect(() => {
        const fetchWorkout = async () => {
        try {
            const response = await axios.get("/api/workouts/1");
            setWorkout(response.data);
            initializeResults(response.data.training_segments.map((segment:TrainingSegments) => segment.exercises).flat());
        } catch (err) {
            setError(`Не удалось загрузить тренировку ${err}`);

        } finally {
            setLoading(false);
        }
        };

        fetchWorkout();
    }, []);

    // Инициализация структуры для результатов
    const initializeResults = (exercises: Exercise[]) => {
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
      field: "actual_weight" | "actual_reps",
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

    return (
        <>
            <Workout>
                <Title marginBottom="10">{workout.tags.map((tag) => tag.name).join(", ")}</Title>
                <Wrapper>
                    <Ul>
                        {workout.training_segments.map((segment) => segment.exercises.map((exercise, index) => (
                          index === activeIndex ? (
                            <Li $borderTop key={index}>
                              <TitleExerciseButton as="span" isActive>
                                <Title marginBottom="10" as="h2">{exercise.name}</Title>
                              </TitleExerciseButton>

                              <ExerciseSetsOl style={{height}}>
                                <Content ref={openContent}>
                                  {results[index].sets.map((set, setIndex)=> (
                                      <Li key={setIndex}>
                                          <Set
                                              key={setIndex}
                                              exercise={exercise}
                                              set={set}
                                              setIndex={setIndex}
                                              onSetChange={handleSetChange}
                                          />
                                      </Li>
                                  ))}
                                </Content>
                              </ExerciseSetsOl>
                            </Li>) : (
                            <Li $borderTop key={index}>
                              <TitleExerciseButton onClick={() => setActiveIndex(index)}>
                                <Title marginBottom="10" as="h2">{exercise.name}</Title>
                              </TitleExerciseButton>

                              <ExerciseSetsOl>
                                <Content>
                                  {results[index].sets.map((set, setIndex)=> (
                                      <Li key={setIndex}>
                                          <Set
                                              key={setIndex}
                                              exercise={exercise}
                                              set={set}
                                              setIndex={setIndex}
                                              onSetChange={handleSetChange}
                                          />
                                      </Li>
                                  ))}
                                </Content>
                              </ExerciseSetsOl>
                            </Li>
                            )
                        )))}

                    </Ul>
                </Wrapper>
            </Workout>
        </>
    )
}
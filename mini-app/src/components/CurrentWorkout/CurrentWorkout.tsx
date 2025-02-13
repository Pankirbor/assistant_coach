import React, {useEffect, useState} from "react";
// import Workout from "../../mock.tsx";
import "./style.css"
import axios from "axios";


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
    weight: number;
    reps: number;
  }[];
}

// const CurrentWorkout = () => {
//     const response = axios.get("/api/workouts/2")
//                         .then(response => response.data)
//                         .catch(error => console.error(error));
//     return (
//         <div>
//             <div>
//                 <h1>Current Workout Data</h1>
//                 <div>{JSON.stringify(response)}</div>
//             </div>
//         </div>
//       )
// }
const CurrentWorkout = () => {
    const [workout, setWorkout] = useState<Workout | null>(null);
    const [results, setResults] = useState<ExerciseResult[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");
    console.log("This line run")
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

//?  interface Set {
//?     target_weight: string;
//?     terget_reps: number;
//?     actual_weight: string;
//?     actual_reps: number;
//?     comment: string,
//?     is_last: boolean;
//? }

  // Инициализация структуры для результатов
  const initializeResults = (exercises: Exercise[]) => {
    const initialResults = exercises.map((exercise) => ({
      exerciseId: exercise.id,
      sets: Array(exercise.target_sets).fill({ weight: 0, reps: 0 }),
    }));
    setResults(initialResults);
  };

  // Обработчик изменения данных подхода
  const handleSetChange = (
    exerciseId: number,
    setIndex: number,
    field: "weight" | "reps",
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
    <div className="workout-container">
      <h2>{workout.tags.map((tag) => tag.name).join(", ")}</h2>
      <p>Дата: {new Date(workout.date).toLocaleDateString()}</p>
      <ol className="circle-list">
        {workout.training_segments.map((segment) => segment.exercises.map((exercise, index) => (
            <ExerciseForm
            key={exercise.id}
            exercise={exercise}
            results={results[index]}
            onSetChange={handleSetChange}
            />
        )))}
      </ol>
      <button onClick={handleSubmit} className="submit-button">
        Готово
      </button>
    </div>
  );
};

//* Компонент для ввода результатов упражнения
const ExerciseForm: React.FC<{
  exercise: Exercise;
  results: ExerciseResult;
  onSetChange: (
    exerciseId: number,
    setIndex: number,
    field: "weight" | "reps",
    value: string
  ) => void;
}> = ({ exercise, results, onSetChange }) => {
  return (
    <li className="exercise-card">
      <h3 className="exercise-name">{exercise.name}</h3>
      <div className="sets-container">
        {results.sets.map((set, setIndex) => (
          <div key={setIndex} className="set-input-group">
            <span>Подход {setIndex + 1}</span>
            <p className="expected-result">{exercise.target_weight}*{exercise.target_reps}</p>
            <input
              type="number"
              placeholder="Вес"
              value={set.weight || ""}
              onChange={(e) =>
                onSetChange(exercise.id, setIndex, "weight", e.target.value)
              }
            />
            <input
              type="number"
              placeholder="Повторения"
              value={set.reps || ""}
              onChange={(e) =>
                onSetChange(exercise.id, setIndex, "reps", e.target.value)
              }
            />
          </div>
        ))}
      </div>
    </li>
  );
};




// const TrainingGrid: React.FC = () => {
//     let exersiseData = Workout.training_segments[0].exercises
//     exersiseData.forEach((ex, id) => ex.results.push(...Array(ex.target_sets).fill({order:id, clientResult: "", completed: false })))
//     const [exercises, setExercises] = useState(exersiseData);

//   const maxApproaches = Math.max(
//     ...exercises.map((ex) => ex.target_sets)
//   );


//   const handleApproachChange = (
//     exerciseId: number,
//     approachIndex: number,
//     value: string
//   ) => {
//     setExercises(
//       exercises.map((ex) =>
//         ex.id === exerciseId
//           ? {
//               ...ex,
//               athleteApproaches: ex.results.map((a, idx) =>
//                 idx === approachIndex ? value : a
//               ),
//             }
//           : ex
//       )
//     );
//   };

//   const toggleCompleted = (exerciseId: number, approachIndex: number) => {
//     setExercises(
//       exercises.map((ex) =>
//         ex.id === exerciseId
//           ? {
//               ...ex,
//               completed: ex.results.map((completed, idx) =>
//                 idx === approachIndex ? !completed : completed
//               ),
//             }
//           : ex
//       )
//     );
//   };

//   return (
//     <div className="training-grid">
//       <div className="header">
//         <h2>СЕГОДНЯ</h2>
//         <div className="date">24.02.2014</div>
//       </div>

//       <div className="grid-container">
//         <div className="grid-header number">№</div>
//         <div className="grid-header exercise">УПРАЖНЕНИЯ</div>
//         {Array.from({ length: maxApproaches }, (_, i) => (
//           <div key={i} className="grid-header approach">
//             {i + 1}
//           </div>
//         ))}

//         {exercises.map((exercise) => (
//           <React.Fragment key={exercise.id}>
//             <div className="grid-item number">{exercise.id}</div>
//             <div className="grid-item exercise">{exercise.name}</div>

//             {Array(exercise.target_sets).fill(`${exercise.target_weight} * ${exercise.target_reps}`).map((approach, idx) => (
//               <div key={idx} className="grid-item coach-approach">
//                 {approach}
//               </div>
//             ))}

//             {/* Пустые ячейки если подходов меньше */}
//             {Array.from({
//               length: maxApproaches - exercise.target_sets,
//             }).map((_, idx) => (
//               <div key={idx} className="grid-item empty">
//                 -
//               </div>
//             ))}

//             <div className="grid-item exercise athlete-inputs" />
//             {Array(exercise.target_sets).map((approach, idx) => (
//               <div key={idx} className="grid-item athlete-approach">
//                 <input
//                   type="text"
//                   value={approach}
//                   onChange={(e) =>
//                     handleApproachChange(exercise.id, idx, e.target.value)
//                   }
//                   placeholder={approach}
//                   className={exercise.results[idx].completed ? "completed" : ""}
//                 />
//                 <button
//                   onClick={() => toggleCompleted(exercise.id, idx)}
//                   className={`check-button ${
//                     exercise.results[idx].completed ? "active" : ""
//                   }`}
//                 ></button>
//               </div>
//             ))}

//             {/* <div
//               className="notes"
//               style={{ gridColumn: `1 / span ${maxApproaches + 2} ` }}
//             >
//               <div className="coach-note">Тренер: {exercise.notes.coach}</div>
//               {exercise.notes.athlete && (
//                 <div className="athlete-note">
//                   Спортсмен: {exercise.notes.athlete}
//                 </div>
//               )}
//             </div> */}
//           </React.Fragment>
//         ))}
//       </div>
//     </div>
//   );
// };

// export default TrainingGrid;

export default CurrentWorkout;
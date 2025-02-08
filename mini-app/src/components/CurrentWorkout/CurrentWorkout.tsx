import React, { useState } from "react";
import Workout from "../../mock.tsx";
import "./style.css"

const TrainingGrid: React.FC = () => {
    let exersiseData = Workout.training_segments[0].exercises
    exersiseData.forEach((ex, id) => ex.results.push(...Array(ex.target_sets).fill({order:id, clientResult: "", completed: false })))
    const [exercises, setExercises] = useState(exersiseData);

  const maxApproaches = Math.max(
    ...exercises.map((ex) => ex.target_sets)
  );


  const handleApproachChange = (
    exerciseId: number,
    approachIndex: number,
    value: string
  ) => {
    setExercises(
      exercises.map((ex) =>
        ex.id === exerciseId
          ? {
              ...ex,
              athleteApproaches: ex.results.map((a, idx) =>
                idx === approachIndex ? value : a
              ),
            }
          : ex
      )
    );
  };

  const toggleCompleted = (exerciseId: number, approachIndex: number) => {
    setExercises(
      exercises.map((ex) =>
        ex.id === exerciseId
          ? {
              ...ex,
              completed: ex.results.map((completed, idx) =>
                idx === approachIndex ? !completed : completed
              ),
            }
          : ex
      )
    );
  };

  return (
    <div className="training-grid">
      <div className="header">
        <h2>СЕГОДНЯ</h2>
        <div className="date">24.02.2014</div>
      </div>

      <div className="grid-container">
        <div className="grid-header number">№</div>
        <div className="grid-header exercise">УПРАЖНЕНИЯ</div>
        {Array.from({ length: maxApproaches }, (_, i) => (
          <div key={i} className="grid-header approach">
            {i + 1}
          </div>
        ))}

        {exercises.map((exercise) => (
          <React.Fragment key={exercise.id}>
            <div className="grid-item number">{exercise.id}</div>
            <div className="grid-item exercise">{exercise.name}</div>

            {Array(exercise.target_sets).fill(`${exercise.target_weight} * ${exercise.target_reps}`).map((approach, idx) => (
              <div key={idx} className="grid-item coach-approach">
                {approach}
              </div>
            ))}

            {/* Пустые ячейки если подходов меньше */}
            {Array.from({
              length: maxApproaches - exercise.target_sets,
            }).map((_, idx) => (
              <div key={idx} className="grid-item empty">
                -
              </div>
            ))}

            <div className="grid-item exercise athlete-inputs" />
            {Array(exercise.target_sets).map((approach, idx) => (
              <div key={idx} className="grid-item athlete-approach">
                <input
                  type="text"
                  value={approach}
                  onChange={(e) =>
                    handleApproachChange(exercise.id, idx, e.target.value)
                  }
                  placeholder={approach}
                  className={exercise.results[idx].completed ? "completed" : ""}
                />
                <button
                  onClick={() => toggleCompleted(exercise.id, idx)}
                  className={`check-button ${
                    exercise.results[idx].completed ? "active" : ""
                  }`}
                ></button>
              </div>
            ))}

            {/* <div
              className="notes"
              style={{ gridColumn: `1 / span ${maxApproaches + 2} ` }}
            >
              <div className="coach-note">Тренер: {exercise.notes.coach}</div>
              {exercise.notes.athlete && (
                <div className="athlete-note">
                  Спортсмен: {exercise.notes.athlete}
                </div>
              )}
            </div> */}
          </React.Fragment>
        ))}
      </div>
    </div>
  );
};

export default TrainingGrid;
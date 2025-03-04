//* Типы для данных клиента
export interface ClientProps {
  id: number;
  telegram_id: number;
  username: string;
  first_name: string;
  last_name: string;
  email: string;
}

export interface TagProps {
      id: number;
      name: string;
      slug: string;
}

export interface SetProps {
    target_weight?: string;
    terget_reps?: number;
    actual_weight: string | number;
    actual_reps: string | number;
    comment?: string,
    is_last?: boolean;
}

export interface ExerciseProps {
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

export interface TrainingSegmentsProps {
      timing: string;
      is_circle: boolean;
      number_laps: number;
      exercises: ExerciseProps[];

}

export interface WorkoutProps {
  id: number;
  date: string;
  client: ClientProps;
  tags: TagProps[];
  timing: string;
  training_segments: TrainingSegmentsProps[]
}

export interface ExerciseResultProps {
  exerciseId: number;
  sets: SetProps[];
}
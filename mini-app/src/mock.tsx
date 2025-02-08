// src/mocks/mock.tsx

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

interface Exercise {
  id: number;
  exercise_id: number;
  name: string;
  video_link: string;
  timing: string;
  target_weight: string;
  target_reps: number;
  target_sets: number;
  general_order: number;
  is_done: boolean;
  comment: string;
  client_comment: string;
  best_result: string;
  results: Set[]; // Можно уточнить тип в зависимости от ваших данных
}

interface Set {
  order: number;
  recommendation: string;
  clientResult: string;
  completed: boolean;
}

interface TrainingSegment {
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
  training_segments: TrainingSegment[];
}

// Создание объекта с образцами данных
const Workout: Workout = {
  id: 3,
  date: "2025-02-03",
  client: {
    id: 1,
    telegram_id: 0,
    username: "Coach",
    first_name: "",
    last_name: "",
    email: "coach@list.ru"
  },
  tags: [
    {
      id: 2,
      name: "Ноги",
      slug: "nogi"
    },
    {
      id: 4,
      name: "Спина",
      slug: "spina"
    }
  ],
  timing: "00:01:00",
  training_segments: [
    {
      timing: "1",
      is_circle: false,
      number_laps: 1,
      exercises: [
        {
          id: 6,
          exercise_id: 2,
          name: "Приседания со штангой",
          video_link: "video_demonstration/134668dhdh",
          timing: "1",
          target_weight: "200.00",
          target_reps: 3,
          target_sets: 5,
          general_order: 1,
          is_done: false,
          comment: "",
          client_comment: "",
          best_result: "0.00",
          results: []
        },
        {
          id: 7,
          exercise_id: 3,
          name: "Подтягивания на турнике",
          video_link: "video_demonstration/923839ncnznh",
          timing: "1",
          target_weight: "0.00",
          target_reps: 10,
          target_sets: 5,
          general_order: 2,
          is_done: false,
          comment: "",
          client_comment: "",
          best_result: "0.00",
          results: []
        }
      ]
    }
  ]
};

export default Workout;

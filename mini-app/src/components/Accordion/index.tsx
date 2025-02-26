import React, { useRef, useState } from 'react';
import { Li, P, Ul } from '../styled/index.tsx';
import { Content, ExerciseSetsOl, TitleExerciseButton } from '../pages/CurrentWorkoutPage/styles.tsx';
import { Title } from '../ui/Title/styles.tsx';
import { Set } from '../Set/index.tsx';


interface SetResultProps {
    target_weight?: string;
    terget_reps?: number;
    actual_weight: string | number;
    actual_reps: string |number;
    comment?: string,
    is_last?: boolean;
}


// interface ExerciseResultProps {
//   exerciseId: number;
//   sets: {
//     actual_weight: string | number;
//     actual_reps: string | number;
//   }[];
// }

interface ExerciseResultProps {
  exerciseId: number;
  sets: SetResultProps[];
}


interface AccordionItemProps {
  title: string;
  content: ExerciseResultProps;
  onSetChange: (exerciseId: number, setIndex: number, field: string, value: string) => void;
}

interface AccordionProps {
    items: AccordionItemProps[];
}

const AccordionExerciseItem: React.FC<AccordionItemProps> = ({ title, content, onSetChange }) => {
  const [isOpen, setIsOpen] = useState<boolean>(false);
  const contentRef = useRef<HTMLDivElement | null>(null);

  const toggleAccordion = () => {
    setIsOpen(!isOpen);
  };

  const contentHeight = isOpen ? `${contentRef.current?.scrollHeight}px` : "0";

  return (
    <Li $borderTop>
      <TitleExerciseButton as="span" isOpen={isOpen} onClick={toggleAccordion}>
        <Title marginBottom="10" as="h2">{title}</Title>
      </TitleExerciseButton>

      <ExerciseSetsOl style={{height : contentHeight}}>
        <Content ref={contentRef}>
          <P>P.  20 30</P>
          {content.sets.map((set, setIndex)=> (
              <Li key={setIndex}>
                <Set
                  key={setIndex}
                  exerciseId={content.exerciseId}
                  set={set}
                  setIndex={setIndex}
                  onSetChange={onSetChange}
                  />
              </Li>
          ))}
        </Content>
      </ExerciseSetsOl>
    </Li>
  );
};

const Accordion: React.FC<AccordionProps>  = ({items}) => {

  return (
    <Ul>
      {items.map((item, index) => (
        <AccordionExerciseItem key={index} title={item.title} content={item.content} onSetChange={item.onSetChange} />
      ))}
    </Ul>
  );
};

export default Accordion;

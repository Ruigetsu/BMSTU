import re

def lab12_7(array, letter):
    all_sentences = []  # [(предложение, start_line, start_pos, end_line, end_pos), ...]
    
    current_sentence = ""
    start_line = 0
    start_pos = 0
    is_sentence_started = False
    
    for line_idx in range(len(array)):
        line = array[line_idx]
        for char_idx in range(len(line)):
            char = line[char_idx]
            if not is_sentence_started and char.strip():
                start_line = line_idx
                start_pos = char_idx
                is_sentence_started = True
            
            if is_sentence_started:
                current_sentence += char
                if char_idx == len(line) - 1 and char != ".": 
                    current_sentence += " "

            is_digit = False
            if char in '.!?':
                if char == ".": 
                    if line[char_idx-1].isdigit() and line_idx[char_idx+1].isdigit() and char_idx != len(line) - 1:
                        is_digit = True 

                if not is_digit:
                    sentence = current_sentence.strip()
                    if sentence:
                        all_sentences.append((
                            sentence,
                            start_line,
                            start_pos,
                            line_idx,
                            char_idx
                        ))
                    current_sentence = ""
                    is_sentence_started = False
    
    if current_sentence.strip(): #добавляем остаток
        all_sentences.append((
            current_sentence.strip(),
            start_line,
            start_pos,
            len(array) - 1,
            len(array[-1]) - 1
        ))
    
    if not all_sentences:
        return "Не нашлось ни одного предложения\n", array
    
    max_count = -1
    max_sentence = None
    
    for sentence_info in all_sentences:
        sentence = sentence_info[0]

        words = re.findall(r'[a-zA-Zа-яА-ЯёЁ]+', sentence)
        count = sum(1 for word in words if word and word[0].lower() == letter.lower())
        
        if count > max_count:
            max_count = count
            max_sentence = sentence_info
    
    if max_sentence is None:
        return "Не нашлось ни одного предложения с такой буквой\n", array
    
    max_sentence, start_line, start_pos, end_line, end_pos = max_sentence
    new_array = []
    
    for line_idx in range(len(array)):
        line = array[line_idx]
        if line_idx < start_line or line_idx > end_line:
            new_array.append(line)
        elif line_idx == start_line and line_idx == end_line: #предложение в одной строке
            new_line = line[:start_pos] + line[end_pos + 1:]
            if new_line.strip():
                new_array.append(new_line)
        elif line_idx == start_line:
            new_line = line[:start_pos]
            if new_line.strip():
                new_array.append(new_line)
        elif line_idx == end_line:
            new_line = line[end_pos + 1:]
            if new_line.strip():
                new_array.append(new_line)
    return max_sentence, new_array
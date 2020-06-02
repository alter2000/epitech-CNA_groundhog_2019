##
## EPITECH PROJECT, 2019
## cpp_rush3_2019
## File description:
## automated desc ftw
##

NAME = groundhog

all: $(NAME)

$(NAME): $(NAME).py
	ln -sf $< $@

clean:
	echo noop

fclean: clean
	rm -f $(NAME)

re:
	echo noop

.PHONY: all clean fclean re $(NAME)

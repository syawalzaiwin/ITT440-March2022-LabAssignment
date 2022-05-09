#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main(void) {
char name;
  for(int i = 1; i < 5; i++) {
    pid_t pid = fork();

    if(pid == 0) {
	printf("Enter your name: \n");
	scanf("%c", &name);
	printf("Your name is %c \n", name);
      printf("Child process => PPID=%d, PID=%d\n", getppid(), getpid());
      exit(0);
    }
    else  {
	printf("You did a good job! \n");
      printf("Parent process => PID=%d\n", getpid());
      printf("Waiting for child processes to finish...\n");
      wait(NULL);
      printf("child process finished.\n");
    }
  }

  return EXIT_SUCCESS;
}

class Solution:
    def comment(self, input :str ) -> str:
        stack={}
        stack.setdefault('(',[])
        stack.setdefault(')',[])
        #double stack
        for i in range(len(input)):
            if input[i] == '(':
                stack['('].append(i)
        #print(stack)
            elif input[i] == ')':
                if stack['(']:
                    stack['('].pop()
                else:
                    stack[')'].append(i)
        commentstring=[' ']*len(input)
        for m in stack['(']:
            commentstring[m]='x'
        for n in stack[')']:
            commentstring[n]='?'
        print(input)
        print(''.join(commentstring))
Solution.comment(Solution,"bge)))))))))")

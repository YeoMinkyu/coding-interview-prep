import heapq
from collections import deque
from typing import List

"""
You are given two string arrays positive_feedback and negative_feedback, containing the words denoting positive and negative feedback, respectively. Note that no word is both positive and negative.

Initially every student has 0 points. Each positive word in a feedback report increases the points of a student by 3, whereas each negative word decreases the points by 1.

You are given n feedback reports, represented by a 0-indexed string array report and a 0-indexed integer array student_id, where student_id[i] represents the ID of the student who has received the feedback report report[i]. The ID of each student is unique.

Given an integer k, return the top k students after ranking them in non-increasing order by their points. In case more than one student has the same points, the one with the lower ID ranks higher.

 

Example 1:

Input: positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is studious","the student is smart"], student_id = [1,2], k = 2
Output: [1,2]
Explanation: 
Both the students have 1 positive feedback and 3 points but since student 1 has a lower ID he ranks higher.
Example 2:

Input: positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is not studious","the student is smart"], student_id = [1,2], k = 2
Output: [2,1]
Explanation: 
- The student with ID 1 has 1 positive feedback and 1 negative feedback, so he has 3-1=2 points. 
- The student with ID 2 has 1 positive feedback, so he has 3 points. 
Since student 2 has more points, [2,1] is returned.

Link: https://leetcode.com/problems/reward-top-k-students/description/?envType=company&envId=bookingcom&favoriteSlug=bookingcom-all
"""



class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        # scores = [0] * len(student_id)
        scores = []
        positive_set, negative_set = set(positive_feedback), set(negative_feedback)
        
        for id, feedback in enumerate(report): # n
            score = 0
            for word in feedback.split(): # the number of word in the strings of feedback
                if word in positive_set:
                    score += 3
                if word in negative_set:
                    score -= 1
            scores.append((-score, student_id[id]))

        heapq.heapify(scores) # O(logn)

        output = []
        for _ in range(0, k):
            score, id = heapq.heappop(scores)
            output.append(id)

        return output
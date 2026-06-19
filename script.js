const students = ["Rahul","Aman","Priya","Riya","Karan","Ankit","Neha","Puja"];

const marks = [78,88,65,95,72,60,88,74];

const attendance = [85,92,75,90,80,70,88,95];

// Marks Chart
new Chart(document.getElementById("marksChart"), {
    type: "bar",
    data: {
        labels: students,
        datasets: [{
            label: "Marks",
            data: marks
        }]
    }
});

// Attendance Chart
new Chart(document.getElementById("attendanceChart"), {
    type: "bar",
    data: {
        labels: students,
        datasets: [{
            label: "Attendance %",
            data: attendance
        }]
    }
});

// Scatter Chart
new Chart(document.getElementById("scatterChart"), {
    type: "scatter",
    data: {
        datasets: [{
            label: "Attendance vs Marks",
            data: [
                {x:85,y:78},
                {x:92,y:88},
                {x:75,y:65},
                {x:90,y:95},
                {x:80,y:72},
                {x:70,y:60},
                {x:88,y:88},
                {x:95,y:74}
            ]
        }]
    },
    options:{
        scales:{
            x:{
                title:{
                    display:true,
                    text:"Attendance (%)"
                }
            },
            y:{
                title:{
                    display:true,
                    text:"Marks"
                }
            }
        }
    }
});
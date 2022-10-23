function solution(s){
    var answer = true;
    var lst=[...s]
    var pcount=0;
    var ycount=0;
    lst.forEach((s)=>{
        if (s==="p"||s==="P"){
            pcount+=1;}
        else if (s==="y"||s==="Y"){
            ycount+=1;}
    });
    if (pcount===ycount){
        answer=true;
    }
    else{
        answer=false;
    }
    return answer;
}
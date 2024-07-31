function Result({data}) {
    return (
        <div>
            <div>Positive : {data.positive}</div>
            <div>Negative : {data.negative}</div>
            <div>Neutral : {data.neutral}</div>
        </div>
    )
}

export default Result;
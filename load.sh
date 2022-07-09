for i in $(seq 1 100)
do
    sleep 0.01
    echo $i
done | whiptail --title 'Mr. Moon Is Loading' --gauge 'Memory Loading...' 5 100 100

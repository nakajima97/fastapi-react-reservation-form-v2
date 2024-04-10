import { DatePicker, LocalizationProvider } from "@mui/x-date-pickers";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import "dayjs/locale/ja";
import dayjs from "dayjs";
import { Controller, useForm } from "react-hook-form";
import { Button, Container, Grid, TextField } from "@mui/material";
import axios from "axios";
import { useEffect, useState } from "react";

dayjs.locale("ja");

axios.defaults.withCredentials = true;

type ReservationFormData = {
  date: dayjs.Dayjs | null;
  name: string;
  emailAddress: string;
  phoneNumber: string;
};

function App() {
  const {
    register,
    control,
    handleSubmit,
    formState: { errors },
    reset,
  } = useForm({
    defaultValues: { date: null, name: "", emailAddress: "", phoneNumber: "" },
  });

  const [holidays, setHolidays] = useState<string[]>([]);

  useEffect(() => {
    axios.get("http://localhost:8000/holidays").then((res) => {
      setHolidays(res.data.holidays);
    });
  }, []);

  const onSubmit = (data: ReservationFormData) => {
    const postData = {
      reservation_date: data.date?.format("YYYY-MM-DD"),
      name: data.name,
      email_address: data.emailAddress,
      phone_number: data.phoneNumber,
    };

    const header = {
      headers: {
        "Content-Type": "application/json",
        withCredentials: "true",
      },
    };

    axios
      .post("http://localhost:8000/reservations", postData, header)
      .then(() => {
        window.alert("予約が完了しました。");
        reset();
      })
      .catch(() => {
        window.alert("予約に失敗しました。時間をおいて再度お試しください。");
      });
  };

  return (
    <>
      <LocalizationProvider dateAdapter={AdapterDayjs}>
        <Container>
          <form onSubmit={handleSubmit(onSubmit)}>
            <Grid container spacing={2}>
              <Grid item xs={12}>
                <Controller
                  name="date"
                  control={control}
                  rules={{ required: "予約日時を選択してください" }}
                  render={({ field }) => (
                    <DatePicker
                      {...field}
                      label="予約日時"
                      sx={{ width: "100%" }}
                      minDate={dayjs().add(1, "day")}
                      format="YYYY/MM/DD"
                      shouldDisableDate={(date) =>
                        holidays.includes(date.format("YYYY-MM-DD"))
                      }
                      slotProps={{
                        textField: {
                          error: errors.date ? true : false,
                          helperText: errors.date?.message as string,
                        },
                      }}
                    />
                  )}
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  {...register("name", { required: "名前を入力してください" })}
                  label="名前"
                  fullWidth
                  error={errors.name ? true : false}
                  helperText={errors.name?.message as string}
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  {...register("emailAddress", {
                    required: "メールアドレスを入力してください",
                  })}
                  label="メールアドレス"
                  type="email"
                  fullWidth
                  error={errors.emailAddress ? true : false}
                  helperText={errors.emailAddress?.message as string}
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  {...register("phoneNumber", {
                    required: "電話番号を入力してください",
                  })}
                  label="電話番号"
                  fullWidth
                  error={errors.phoneNumber ? true : false}
                  helperText={errors.phoneNumber?.message as string}
                />
              </Grid>
              <Grid item xs={12}>
                <Button type="submit" fullWidth>
                  予約
                </Button>
              </Grid>
            </Grid>
          </form>
        </Container>
      </LocalizationProvider>
    </>
  );
}

export default App;

import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import { z } from "zod";

import { Button } from "@/components/ui/button";
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { useMutation } from "@tanstack/react-query";
import { submitForm } from "@/api";
import { Data } from "@/types";
import React from "react";
import toast from "react-hot-toast";

const formSchema = z.object({
  url: z
    .string()
    .min(1, {
      message: "Please enter a url.",
    })
    .url(),
});

const LinkForm = ({
  setData,
}: {
  setData: React.Dispatch<React.SetStateAction<Data | null>>;
}) => {
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      url: "",
    },
  });

  // Mutations
  const { mutateAsync, isPending } = useMutation({
    mutationFn: submitForm,
    onSuccess: (data) => {
      if (data?.data) {
        setData(data.data);
        form.reset();
      }
    },
    onError: (error) => {
      console.log(error);
    },
  });

  // Form Submit handler
  function onSubmit({ url }: z.infer<typeof formSchema>) {
    const promise = mutateAsync(url);

    toast.promise(
      promise,
      {
        loading: "Scraping the website...",
        success: () => `Successfully scraped ${url}`,
        error: () => "Network error. Please try again later.",
      },
      {
        style: {
          maxWidth: "250px",
        },
      }
    );
  }

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
        <FormField
          control={form.control}
          name="url"
          render={({ field }) => (
            <FormItem>
              <FormLabel>URL</FormLabel>
              <FormControl>
                <Input placeholder="https://example.com" {...field} />
              </FormControl>
              <FormDescription>Please enter a url to scrape.</FormDescription>
              <FormMessage />
            </FormItem>
          )}
        />

        <div className="flex items-center gap-2">
          <Button type="submit" disabled={isPending}>
            {isPending ? "Submitting..." : "Scrape"}
          </Button>
        </div>
      </form>
    </Form>
  );
};

export default LinkForm;
